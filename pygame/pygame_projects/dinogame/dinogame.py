from unittest import runner
import pygame
import sys

pygame.init()
pygame.display.set_caption('Jumping dino')
MAX_WIDTH = 800
MAX_HEIGH = 400

def main():
    screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGH))
    fps = pygame.time.Clock()

    #dino
    imgDino1 = pygame.image.load('images/dinowalk_1.png')
    imgDino1 = pygame.image.load('images/dinowalk_2.png')
    dino_height = imgDino1.get_size()[1]
    dino_bottom = MAX_HEIGH - dino_height
    dino_x = 50
    dino_y = dino_bottom
    jump_top = 200
    leg_swap = True
    is_bottom = True
    is_go_up = False

    # tree
    imgTree = pygame.image.load('images/tree_b_1.png')
    tree_height = imgTree.get_size()[1]
    tree_x = MAX_WIDTH
    tree_y = MAX_HEIGH - tree_height

    running = True
    while running:
        screen.fill((255,255,255))

        # event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if is_bottom:
                    is_go_up = True
                    is_bottom = False

        # dino move
        if is_go_up:
            dino_y -= 10.0
        elif not is_go_up and not is_bottom:
            dino_y += 10.0

        # dino top and bottom check
        if is_go_up and dino_y <= jump_top:
            is_go_up = False
        
        if not is_bottom and dino_y >= dino_bottom:
            is_bottom = True
            dino_y = dino_bottom

        tree_x -= 12.0
        if tree_x <= 0:
            tree_x = MAX_WIDTH

        # 좌표처리
        dino_rect = imgDino1.get_rect()
        dino_rect.left = dino_x
        dino_rect.right = dino_y

        tree_rect = imgTree.get_rect()
        tree_rect.left = tree_x
        tree_rect.right = tree_y


        # 충돌 체크
        if dino_rect.collidedict(tree_rect):
            print("충돌했습니다")
            running = False

        # 화면 출력
        screen.blit(imgTree,(tree_x, tree_y))
        
        # draw tree
        if leg_swap:
            screen.blit(imgDino1, (dino_x, dino_y))
            leg_swap = False
        else:
            screen.blit(imgDino1, (dino_x, dino_y))
            leg_swap = True

        # update
        pygame.display.update()
        fps.tick(30)

if __name__ == '__main__':
    main()